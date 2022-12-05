import React, { useState } from "react";
import axios from "axios";

import "./App.css";

const endpoint = "http://127.0.0.1:8000/imagen";

function App() {
  const [image, setImage] = useState(null);
  const [name, setName] = useState();

  const onImageChange = (event) => {
    if (event.target.files && event.target.files[0]) {
      setImage(URL.createObjectURL(event.target.files[0]));
    }
  };

  const predict = async (e) => {
    e.preventDefault();

    const response = await axios.post(
      endpoint,{
        image: image
      }
    );
    console.log(response);
  };


  return (
    <div className="m-2 md:m-10 p-2  md:p-10 bg-white rounded-3xl">
      <div className="md:grid md:grid-cols-2 md:gap-10">
        <div className="mt-5 md:col-start-1 pl-20">
          <img src={image} alt="Logo" />
        </div>
        <div className="mt-5 md: col-start-2 md:mt-0">
          <form className="w-full max-w-sm " onSubmit={predict}>
            <div className="flex items-center border-b border-teal-500 py-2 pt-20">
              <input
                className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                type="file"
                accept="image/png, image/gif, image/jpeg"
                aria-label="imagen"
                onChange={onImageChange}
              />
              <button
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
                type="submit"
              >
                Usar
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default App;
