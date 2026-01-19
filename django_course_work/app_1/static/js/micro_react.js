document.addEventListener("DOMContentLoaded", () => {

    function createStore(initialState) {
        let state = { ...initialState };
        const listeners = new Set();

        function set(patch) {
            Object.assign(state, patch);
            listeners.forEach(fn => fn(state));
        }

        function subscribe(fn) {
            listeners.add(fn);
            fn(state);
            return () => listeners.delete(fn);
        }

        return { set, subscribe };
    }

    function bindText(store) {
        store.subscribe(state => {
            document.querySelectorAll("[data-bind]").forEach(el => {
                const key = el.dataset.bind;
                if (key in state) {
                    el.textContent = state[key];
                }
            });
        });
    }

    function bindProgressBars(store) {
        store.subscribe(state => {
            document.querySelectorAll("[data-progress]").forEach(el => {
                const key = el.dataset.progress;
                if (key in state) {
                    el.style.setProperty("--progress", state[key] + "%");
                }
            });
        });
    }

    const body = document.body;

    const store = createStore({
        time: body.dataset.initialTime,
        progress: parseInt(body.dataset.initialProgress, 10)
    });

    bindText(store);
    bindProgressBars(store);

    const updateUrl = body.dataset.updateUrl;

    setInterval(() => {
        fetch(updateUrl)
            .then(r => r.json())
            .then(data => {
                store.set({
                    time: parseInt(data.time),
                    progress: parseInt(data.progress)
                });
            })
            .catch(err => console.error("Update failed:", err));
    }, 100);
});
