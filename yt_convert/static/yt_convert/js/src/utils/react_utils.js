const renderReactDom = (containerID, component) => {
    const container = document.getElementById(containerID);
    try {
        ReactDOM.createRoot(container).render(component);
    } catch (error) {
        console.log('Add React CDN links first before adding this script');
    }
}