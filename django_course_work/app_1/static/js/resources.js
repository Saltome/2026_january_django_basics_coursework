const updateUrl = document.body.dataset.updateUrl;

const state = {
    time: document.getElementById('time').textContent,
    progress: parseInt(document.getElementById('progress-text').textContent, 10)
};

function render() {
    document.getElementById('time').textContent = state.time;
    document.getElementById('time_progress_bar')
        .style.setProperty('--progress', state.progress + '%');
    document.getElementById('progress-text').textContent =
        "Progress: " + state.progress + "%";
}

function updateState() {
    fetch(updateUrl)
        .then(r => r.json())
        .then(data => {
            state.time = parseInt(data.time);
            state.progress = parseInt(data.progress);
            render();
        });
}

setInterval(updateState, 100);
