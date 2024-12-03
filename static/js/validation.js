// Owner Sign-Up Form Validation
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const phoneInput = document.getElementById("phone");

    form.addEventListener("submit", function (e) {
        const phonePattern = /^[0-9]{10}$/;
        if (!phonePattern.test(phoneInput.value)) {
            e.preventDefault();
            alert("Please enter a valid 10-digit phone number.");
        }
    });
});
