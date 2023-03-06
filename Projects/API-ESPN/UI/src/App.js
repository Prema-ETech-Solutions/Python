import React from "react";
import "./App.css"

function App() {
  return (
    <>
      <div className="App">
        <form
          className="App"
          action="http://127.0.0.1:5000/upload/csv" method="POST" encType="multipart/form-data"
          >
          <input className="file" type="file" name="file" required="true" />
          <input  className="enjoy-css" type="text" name="txt" placeholder="Output File Name " required="true" />
          <input type="submit" className="css-button-3d--rose" />
        </form>
      </div>
      </>
  );
}
export default App;
