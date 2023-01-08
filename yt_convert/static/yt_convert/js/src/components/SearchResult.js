'use strict';

class SearchResult extends React.Component {
    constructor(props){
        super(props);
        console.log(props);
    }
    getYtInfo = (attrName) => {
        return this.props.ytInfo[attrName];
    }
    render() {
        return (
            <React.Fragment>
                <img
                    src={this.getYtInfo('thumbnail_url')}
                    style={{
                        height:'166px',
                        borderRadius:'10px',
                        alignSelf:'center'
                    }}
                />
                <div className="yt-details">
                    <div className="yt-body">
                        <h3>Title: {this.getYtInfo('title')}</h3>
                        <p>Author: {this.getYtInfo('author')}</p>
                        <p>Length: {formatVideoLength(this.getYtInfo('length'))}</p>
                    </div>
                    <div className="flex align-items-center"
                        style={{justifyContent: 'space-evenly'}}>
                        <a className="btn" href={this.getYtInfo('dl_url')}>
                            Download {this.getYtInfo('abr')} ({(this.getYtInfo('filesize_mb')).toFixed(2)} MB)
                        </a>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}
const searchResultContainer = document.getElementById('search-results');
const searchResultRoot = ReactDOM.createRoot(searchResultContainer);
