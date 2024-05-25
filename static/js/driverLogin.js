document.addEventListener("DOMContentLoaded", function () {
    let currentStep = 1;
    const formSections = document.querySelectorAll(".form-section");
    const progress = document.getElementById("progress");

    function showStep(step) {
        formSections.forEach((section, index) => {
            section.style.display = index === step - 1 ? "block" : "none";
        });
        progress.style.width = `${180 * step}px`;
    }

    document.getElementById("next1").addEventListener("click", function () {
        currentStep = 2;
        showStep(currentStep);
    });

    document.getElementById("back1").addEventListener("click", function () {
        currentStep = 1;
        showStep(currentStep);
    });

    showStep(currentStep); // Initialize the form to show the first step
});