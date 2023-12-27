let form=document.getElementById("my_form")
let table=document.getElementById("my_table")
form.addEventListener("submit",function(e){
  e.preventDefault();
  let first_name=document.getElementById("first name").value
  let last_name=document.getElementById("last name").value
  let email=document.getElementById("email").value
  if(first_name.length==0 || last_name.length==0 || email.length==0){
    document.getElementById("error").innerHTML="fill all fields"
  }else{
    let new_row=table.insertRow()
    new_row.insertCell(0).textContent=first_name
    new_row.insertCell(1).textContent=last_name
    new_row.insertCell(2).textContent=email
  }
  form.reset()
})