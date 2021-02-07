const searchTeam=async () => {
    nteam = document.getElementById("nteam")
    console.log('nteam',nteam)
    const response = await fetch('http://localhost:5000/?id='+nteam.value);
    console.log(response)
    const myJson = await response.json(); //extract JSON from the http response
    console.log(myJson)
    a=JSON.stringify(myJson)
    obj=JSON.parse(a)
    arr=Object.values(obj)
    b=obj.nombre
    ob=JSON.stringify(b)
    obj1=JSON.parse(ob)
    console.log(obj1)
    for (var key in obj1) {
  
        c=obj1[nteam.value];
      }
    var cambiar;
    cambiar=document.getElementById("cambiar");
    cambiar.innerHTML=c;
    pun=obj.puntos
    ob1=JSON.stringify(pun)
    obj2=JSON.parse(ob1)
    console.log(obj2)
    for (var key in obj2) {
  
      d=obj2[nteam.value];
    }
    var cambiar;
    cambiar=document.getElementById("chan");
    cambiar.innerHTML=d;
    
    esc=obj.link
    ob2=JSON.stringify(esc)
    obj3=JSON.parse(ob2)
    for (var key in obj3) {
  
      e=obj3[nteam.value];
    }
    console.log(e)
    document.getElementById("imgchange").src= "https://"+e

    
}