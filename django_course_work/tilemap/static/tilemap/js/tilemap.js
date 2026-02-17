document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("tilemap-container");

    const width = 20;
    const height = 20;

    for (let y = 0; y < height; y++) {
        const row = document.createElement("div");
        row.classList.add("tile-row");

        for (let x = 0; x < width; x++) {
            const tile = document.createElement("div");
            tile.classList.add("tile");
            tile.dataset.x = x;
            tile.dataset.y = y;

            tile.addEventListener("click", function () {
                tile.classList.toggle("active");
            });

            row.appendChild(tile);
        }

        container.appendChild(row);
    }
});
