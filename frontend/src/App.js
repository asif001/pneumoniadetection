import React from 'react';
import axios from 'axios';
import './App.css';

class App extends React.Component{


	constructor(props) {
	    super(props);
	      this.state = {
		selectedFile: null,
                diagnosis: null,
	      }
	   
	  }

	onChangeHandler=event=>{
	    this.setState({
	      selectedFile: event.target.files[0],
	      loaded: 0,
	      diagnosis: null,
	    })
	  }

	onClickHandler = () => {
	    const data = new FormData() 
	    data.append('file', this.state.selectedFile)
	    axios.post("http://34.66.216.62:5000/predict", data, { 
      		// receive two    parameter endpoint url ,form data
	  }).then((res) => { // then print response status
            this.setState({diagnosis: res.data})
	 })
	}

   
	render(){

		return (	
		   <div className="container">
			<div className="row">
			   <div className="col-md-6">
			      <form method="post" action="#" id="#">
			      <div className="form-group files color">
				<label>Upload Your File </label>
				<input type="file" name="file" className="form-control" multiple="" onChange={this.onChangeHandler}/>
			      </div>
			  </form>
			<button type="button" className="btn btn-success btn-block" onClick={this.onClickHandler}>Upload</button>
			<p>The result is : {this.state.diagnosis}</p>   
			  </div>
			</div>
		   </div>
		  );
	}


}

export default App;
