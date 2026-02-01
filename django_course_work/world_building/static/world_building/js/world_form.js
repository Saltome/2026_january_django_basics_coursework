document.addEventListener("DOMContentLoaded", function () {
    const randomBtn = document.getElementById("random-seed-btn");

    if (!randomBtn) return;

    randomBtn.addEventListener("click", async function () {
        const seedField = document.getElementById("id_seed");
        const nameField = document.getElementById("id_name");

        if (!seedField || !nameField) return;

        const seed = Math.random();
        seedField.value = seed;

        try {
            const response = await fetch(
                `${GENERATE_WORLD_NAME_URL}?seed=${encodeURIComponent(seed)}`
            );
            const data = await response.json();

            nameField.value = data.name;
        } catch (error) {
            console.error("Failed to generate world name:", error);
        }
    });
});
