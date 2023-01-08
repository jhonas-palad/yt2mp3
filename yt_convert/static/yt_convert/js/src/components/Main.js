'use strict';

const FETCH_URL = '/fetch_yt/';

const searchResultContainer = document.getElementById('search-results');

class SearchButton extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            disabled: false,
            showErr: false,
            errMsg: '',
            isLoading: false,
        }
    }
    getInputUrl = () => {
        const yt_url = document.getElementById('id_yt_url');
        const {value} = yt_url;
        if(!value || /^$/.test(value)){
            throw new Error('Please enter a YouTube URL');
        }

        this.setState({
            showErr: false
        });
        return {
            yt_url : value
        }
    }
    handleOnClick = async (e) => {
        try{
            this.setState({isLoading: true, disabled: true});
            const post_data = this.getInputUrl();
            const opts = {
                method: 'POST',
                header: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(post_data)
            }
            const response = await fetch(FETCH_URL, opts);
            const data = await response.json();
            if (!response.ok && response.status != 200){
                throw new Error(data.err_msg);
            }
            searchResultRoot.render(
                <SearchResult
                    ytInfo={data}
                />
            )
                
            console.log(response);
            console.log(data);
        }
        catch (err){
            this.setState({
                showErr: true,
                errMsg: err.message
            })
        }
        finally{
            this.setState({isLoading: false, disabled: false});
        }
    }
    render(){
        return(
            <React.Fragment>
                {
                    this.state.showErr ? (
                        <span err-msg="">{this.state.errMsg || 'Something went wrong!'}</span>
                    ) : (
                        null
                    )
                }
                {
                    this.state.isLoading ? (
                        <React.Fragment>

                        <span 
                            id="search_loader"  
                            className="loader-jump-split margin-top-1"></span>
                        <p>
                            Converting please wait...
                        </p>
                        </React.Fragment>
                    ) : (
                        <button 
                            id="id_search_btn" 
                            className="btn"
                            type="button"
                            onClick={this.handleOnClick}
                            disabled={this.state.disabled}
                        >
                        Convert
                        </button>
                    )
                }
            </React.Fragment>
        )
        
    }
}

renderReactDom('search-button', <SearchButton/>);
