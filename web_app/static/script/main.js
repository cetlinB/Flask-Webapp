
function getAllNamesIntoTable(){
    let names;
    fetch('http://127.0.0.1:5000/get_all_users/logins')
        .then( (response) => {
            response.text().then((text) =>{
                names = JSON.parse(text);
                console.log(names);
                for(let i = 0; i<names.logins.length; i++){
                    putNamesIntoTable(names.logins[i]);
                }
            });
        })
        .catch( (ex) => {
            console.log('Connection failed', ex);
         });

}

function putNamesIntoTable(name) {
    let tbodys = document.getElementsByTagName("tbody");
    let size = (tbodys[0]).children.length;
    (tbodys[0]).innerHTML += "<tr><td>" + (size + 1) + "</td><td>" + name + "</td></tr>";
}

getAllNamesIntoTable();
