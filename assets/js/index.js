var React = require('react')
var ReactDOM = require('react-dom')

var RoomsList = React.createClass({
    loadRoomsFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadRoomsFromServer();
        setInterval(this.loadRoomsFromServer, 
                    this.props.pollInterval)
    }, 
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var roomNodes = this.state.data.map(function(room){
                return <li> {room.code} </li>
            })
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {roomNodes}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<RoomsList url='/api/v1/room' pollInterval={1000} />, 
    document.getElementById('container'))
