// Get the button from HTML

const skillsButton =
    document.getElementById("skillsButton");


// When the button is clicked

skillsButton.addEventListener("click", function () {

    // Find the Skills section

    const skillsSection =
        document.getElementById("skills");

    // Scroll to Skills

    skillsSection.scrollIntoView({
        behavior: "smooth"
    });

});