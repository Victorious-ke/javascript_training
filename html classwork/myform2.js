// addEventListener
// document.innerHTML
  // get form to javascript
 let form = document.getElementById("my_form");
 let table = document.getElementById("my_table");
  // add event to form

  form.addEventListener("submit",function(e){
    // prevent page from refreshing
    e.preventDefault()
    // check user input
    let first_name = document.getElementById("first_name").value
    let last_name = document.getElementById("last_name").value
    let email = document.getElementById("email").value
    if(first_name.length==0 || last_name==0 || email==0){
      document.getElementById("error").innerHTML= "fill all fields"
    }
    else{
      let row= table.insertRow()
      row.insertCell(0).textContent= first_name
      row.insertCell(1).textContent= last_name
      row.insertCell(2).textContent= email
    }
    form.reset()
  });
  
