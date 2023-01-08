const searchBtn = document.getElementById('id_search_btn');
const loaderSpinner = document.getElementById('search_loader');
const searchInput = document.getElementById('id_yt_url');
const errSpan = document.querySelector('span[err-msg]');
const errSpanParent = errSpan.parentElement;

const toggleLoadButton = () => {
    loaderSpinner.classList.toggle('hidden');
    searchBtn.classList.toggle('hidden');
}

const fetchAudio = async () => {
    toggleLoadButton();
    searchBtn.disabled=true;
    searchBtn.removeEventListener('click', fetchAudio);
    try{
        const yt_url = searchInput.value;
        const post_data = { yt_url };
        const response = await fetch('fetch_yt/', {
            method:'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(post_data)
        });
        const data = await response.json();
        console.log(response);
        console.log(data);

        if(!response?.ok && response.status !== 200)
            throw new Error(data.err_msg);
        
        errSpanParent.classList.contains('invalid') && errSpanParent.classList.remove('invalid');
    }
    catch(err) {
        //Network error
        errSpan.innerHTML = err.message;
        errSpan.parentElement.classList.add('invalid');
    }
    finally{
        searchBtn.addEventListener('click', fetchAudio);
        searchBtn.disabled=false;    
        toggleLoadButton();
    }
}

searchBtn.addEventListener('click', fetchAudio);

