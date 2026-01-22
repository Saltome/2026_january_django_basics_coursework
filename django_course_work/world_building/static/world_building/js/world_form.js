document.addEventListener("DOMContentLoaded", function() {
    const randomBtn = document.getElementById("random-seed-btn");
    if (randomBtn) {
        randomBtn.addEventListener("click", function() {
            const seedField = document.getElementById("id_seed");
            if (seedField) {
                seedField.value = Math.random(); // Random float 0–1
            }
        });
    }
});
