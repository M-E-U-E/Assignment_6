from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import PropertyOwner
from django.conf import settings


class TestViews(TestCase):
    #settings.py
    def test_debug_mode(self):
        # Check DEBUG setting
        self.assertTrue(hasattr(settings, 'DEBUG'))
        self.assertIn(settings.DEBUG, [True, False])

    def test_secret_key(self):
        # Ensure SECRET_KEY is set
        self.assertTrue(hasattr(settings, 'SECRET_KEY'))
        self.assertNotEqual(settings.SECRET_KEY, '')
        self.assertNotEqual(settings.SECRET_KEY, 'django-insecure')

    def test_allowed_hosts(self):
        # Check ALLOWED_HOSTS
        self.assertTrue(hasattr(settings, 'ALLOWED_HOSTS'))
        self.assertIsInstance(settings.ALLOWED_HOSTS, list)

    def test_installed_apps(self):
        # Ensure INSTALLED_APPS includes essential apps
        essential_apps = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.gis',  # Specific to your settings
            'properties',  # Custom app
            'import_export',  # Third-party app
        ]
        for app in essential_apps:
            self.assertIn(app, settings.INSTALLED_APPS)

    def test_middleware(self):
        # Check essential middleware
        essential_middleware = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]
        for middleware in essential_middleware:
            self.assertIn(middleware, settings.MIDDLEWARE)

    def test_templates(self):
        # Verify TEMPLATES configuration
        self.assertTrue(hasattr(settings, 'TEMPLATES'))
        self.assertIsInstance(settings.TEMPLATES, list)
        template_dirs = settings.TEMPLATES[0].get('DIRS', [])
        self.assertIn(settings.BASE_DIR / 'templates', template_dirs)
        self.assertTrue(settings.TEMPLATES[0].get('APP_DIRS', False))

    def test_static_files(self):
        # Check STATIC_URL and STATICFILES_DIRS
        self.assertTrue(hasattr(settings, 'STATIC_URL'))
        self.assertTrue(settings.STATIC_URL.startswith('/'))
        self.assertTrue(hasattr(settings, 'STATICFILES_DIRS'))
        self.assertIn(settings.BASE_DIR / 'static', settings.STATICFILES_DIRS)

    def test_database_config(self):
        # Validate DATABASES settings
        self.assertTrue(hasattr(settings, 'DATABASES'))
        default_db = settings.DATABASES['default']
        self.assertEqual(default_db['ENGINE'], 'django.contrib.gis.db.backends.postgis')
        self.assertTrue(default_db['NAME'])  # Check database name is set
        self.assertTrue(default_db['USER'])  # Check database user is set
        self.assertTrue(default_db['PASSWORD'])  # Check database password is set
        self.assertTrue(default_db['HOST'])  # Check database host is set
        self.assertTrue(default_db['PORT'])  # Check database port is set

    def test_auth_password_validators(self):
        # Check AUTH_PASSWORD_VALIDATORS
        self.assertTrue(hasattr(settings, 'AUTH_PASSWORD_VALIDATORS'))
        self.assertIsInstance(settings.AUTH_PASSWORD_VALIDATORS, list)
        validators = [
            'UserAttributeSimilarityValidator',
            'MinimumLengthValidator',
            'CommonPasswordValidator',
            'NumericPasswordValidator',
        ]
        for validator in validators:
            self.assertTrue(
                any(validator in v['NAME'] for v in settings.AUTH_PASSWORD_VALIDATORS)
            )

    def test_internationalization(self):
        # Verify language and timezone settings
        self.assertTrue(hasattr(settings, 'LANGUAGE_CODE'))
        self.assertEqual(settings.LANGUAGE_CODE, 'en-us')
        self.assertTrue(hasattr(settings, 'TIME_ZONE'))
        self.assertEqual(settings.TIME_ZONE, 'UTC')
        self.assertTrue(settings.USE_I18N)
        self.assertTrue(settings.USE_TZ)

    def test_login_and_logout_redirects(self):
        # Check LOGIN_REDIRECT_URL and LOGOUT_REDIRECT_URL
        self.assertTrue(hasattr(settings, 'LOGIN_REDIRECT_URL'))
        self.assertEqual(settings.LOGIN_REDIRECT_URL, '/')
        self.assertTrue(hasattr(settings, 'LOGOUT_REDIRECT_URL'))
        self.assertEqual(settings.LOGOUT_REDIRECT_URL, '/')

    def test_default_auto_field(self):
        # Check DEFAULT_AUTO_FIELD
        self.assertTrue(hasattr(settings, 'DEFAULT_AUTO_FIELD'))
        self.assertEqual(settings.DEFAULT_AUTO_FIELD, 'django.db.models.BigAutoField')
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('user_signup')  # Replace with the actual name of the signup URL
        self.login_url = reverse('user_login')  # Replace with the actual name of the login URL
        self.activation_url = reverse('activation')  # Replace with the actual name of the activation URL
        self.owner_signup_url = reverse('owner_signup')  # Replace with the actual name of the owner signup URL
        self.home_url = reverse('home')  # Replace with the actual name of the home URL

    def test_user_signup_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_user_signup_post_success(self):
        response = self.client.post(self.signup_url, {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 200)  # Activation page is rendered
        self.assertTemplateUsed(response, 'activation.html')
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_signup_post_missing_fields(self):
        response = self.client.post(self.signup_url, {
            'username': '',
            'email': '',
            'password': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'All fields are required!')

    def test_user_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_login_post_success(self):
        user = User.objects.create_user(username='testuser', password='password123')
        user.is_active = True
        user.save()

        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to 'home'
        self.assertRedirects(response, self.home_url)

    def test_user_login_post_inactive_user(self):
        user = User.objects.create_user(username='testuser', password='password123')
        user.is_active = False
        user.save()

        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to 'activation'
        self.assertRedirects(response, self.activation_url)

    def test_user_login_post_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'wronguser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Invalid username or password.')

    def test_activation_page(self):
        response = self.client.get(self.activation_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'activation.html')

    def test_owner_signup_get(self):
        response = self.client.get(self.owner_signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'owner_signup.html')

    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to the Inventory Management System!')
