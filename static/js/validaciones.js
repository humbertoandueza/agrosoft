function email(a){  
  return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/.test(a); 
}
function mayus(e) {
    e.value = e.value.toUpperCase();
}
function Teclas(e, accept){
    var ascii = e.which|e.keyCode;
    var ret = false;
    vari1=ascii>=48 && ascii<=57
    vari2=ascii>=65 && ascii<=90 || ascii>=97 && ascii<=122 || ascii==241 || ascii==209 || ascii==32
    if (accept==1){
        if(vari1){
        ret=true;
        }
    }else if (accept==2){
        if (vari2){
        ret=true;
        }
    }else if (accept==3){
        if (vari1 || vari2 || ascii==45 || ascii==95 || ascii==64 || ascii==46){
        ret = true;
        }
    } 
    console.log(ascii);
    return ret;
}


function Validar(e) {
  if(enviar(document.getElementsByName("password")[0]) &&
    enviar(document.getElementsById("cedula")[0]) &&
    enviar(document.getElementsByName("pri_nombre")[0])&&
    enviar(document.getElementsByName("primer_nomb")[0])&&
    enviar(document.getElementsByName("seg_nombre")[0])&&
    enviar(document.getElementsByName("segundo_nomb")[0])&&
    enviar(document.getElementsByName("pri_apellido")[0])&&
    enviar(document.getElementsByName("primer_ape")[0])&&
    enviar(document.getElementsByName("seg_apellido")[0])&&
    enviar(document.getElementsByName("segundo_ape")[0])&&
    enviar(document.getElementsByName("email")[0])&&
    enviar(document.getElementsByName("correo")[0])&&
    enviar(document.getElementsByName("password1")[0])&&
    enviar(document.getElementsByName("password2")[0])&&
    enviar(document.getElementsByName("direccion")[0])&&
    enviar(document.getElementsByName("municipio")[0])&&
    enviar(document.getElementsByName("parroquia1")[0])&&
    enviar(document.getElementsByName("parroquia2")[0])&&
    enviar(document.getElementsByName("parroquia3")[0])&&
    enviar(document.getElementsByName("parroquia4")[0])&&
    enviar(document.getElementsByName("parroquia5")[0])&&
    enviar(document.getElementsByName("parroquia6")[0])&&
    enviar(document.getElementsByName("parroquia7")[0])&&
    enviar(document.getElementsByName("parroquia8")[0])&&
    enviar(document.getElementsByName("parroquia9")[0])&&
    enviar(document.getElementsByName("parroquia10")[0])&&
    enviar(document.getElementsByName("parroquia11")[0])&&
    enviar(document.getElementsByName("parroquia12")[0])&&
    enviar(document.getElementsByName("parroquia13")[0])&&
    enviar(document.getElementsByName("parroquia14")[0])&&
    enviar(document.getElementsByName("sector")[0])&&
    enviar(document.getElementsByName("solicitud")[0])&&
    enviar(document.getElementsByName("identidad")[0])&&
    enviar(document.getElementsByName("nomb_organizacion")[0])&&
    enviar(document.getElementsByName("rif")[0])&&
    enviar(document.getElementsByName("genero")[0])&&
    enviar(document.getElementsByName("codigo")[0])&&
    enviar(document.getElementsByName("nombre")[0])){
    return true;
    }
    return false;
}      
function borrarEspacio(e) {
  var txt = e.value;
  var txta;
  do {
    txta = txt;
    txt = txt.replace("  ", " ");
  } while (txt !== txta);
  e.value = txt.trim();
};
function enviar(ele) {
var val = false;
  var aux, aux2;
  aux = ele;
  borrarEspacio(ele); 
  if(ele.getAttribute("id") == "username"){
    if(aux.value.length>=7 && aux.value.length<=8){
      val=true;
    }else{
      aux2="Este campo debe contener 8 dígitos";
    }
  }else if (ele.getAttribute("name") == "password"){
    if (aux.value.length>=8 && aux.value.length<=16){
      val=true;
    }else{
      aux2="Este campo debe contener mínimo 8 dígitos y máximo 16 dígitos";
    }
  }else if (ele.getAttribute("id") == "cedula"){
    if (aux.value==""){
      val=true;
    }else if (aux.value.length>= 7 && aux.value.length <= 8){
      val=true;
    }else{
      aux2="Este campo debe contener 8 dígitos"
    }  
  }else if(ele.getAttribute("name")=="pri_nombre" || (ele.getAttribute("name")=="pri_apellido") || (ele.getAttribute("name")=="primer_nomb") || (ele.getAttribute("name")=="primer_ape") || (ele.getAttribute("name")=="nomb_organizacion") || (ele.getAttribute("name")=="nombre")){
    if (aux.value.length>=2 && aux.value.length<=30){
      val=true;
    }else{
      aux2="Este campo debe ser mayor a 2 letras"
    }
  }else if(ele.getAttribute("name")=="seg_nombre" || (ele.getAttribute("name")=="seg_apellido") || (ele.getAttribute("name")=="segundo_nomb") || (ele.getAttribute("name")=="segundo_ape")){
    if (aux.value==""){
      val=true;
    }else if (aux.value.length>=2 && aux.value.length<=30){
      val=true;
    }else{
      aux2="Este campo debe ser mayor a 2 letras"
    }
  }else if(ele.getAttribute("name")=="email"|| (ele.getAttribute("name")=="correo")){
    if (email(ele.value)){
      val=true;
    }else{
      aux2="Ingrese un correo electronico"
    }
  }else if (ele.getAttribute("name")=="password1" || (ele.getAttribute("name")=="password2")){
    if (aux.value.length>=8 && aux.value.length<=16){
      val=true;
    }else{
      aux2="Este campo debe contener mínimo 8 dígitos y máximo 16 dígitos";
    }
  }else if (ele.getAttribute("name")=="direccion"){
    if (aux.value.length>=5 && aux.value.length<=150){
      val=tre;
    }else{
      aux2="Este campo debe ser mayor a 5 letras";
    }
  }else if (ele.getAttribute("name")=="telefono"){
    if (aux.value.length>=11 && aux.value.length<=11){
      val=true;
    }else{
      aux2="Este campo debe contener 11 dígitos";
    }
  }else if (ele.getAttribute("name") == "nacionalidad" || (ele.getAttribute("name")=="municipio") || (ele.getAttribute("name")=="parroquia1") || (ele.getAttribute("name")=="parroquia2") || (ele.getAttribute("name")=="parroquia3") || (ele.getAttribute("name")=="parroquia4")|| (ele.getAttribute("name")=="parroquia5") || (ele.getAttribute("name")=="parroquia6") || (ele.getAttribute("name")=="parroquia7") || (ele.getAttribute("name")=="parroquia8") || (ele.getAttribute("name")=="parroquia9") || (ele.getAttribute("name")=="parroquia10") || (ele.getAttribute("name")=="parroquia11") || (ele.getAttribute("name")=="parroquia12") || (ele.getAttribute("name")=="parroquia13") || (ele.getAttribute("name")=="parroquia14") || (ele.getAttribute("name")=="solicitud") || (ele.getAttribute("name")=="identidad") || (ele.getAttribute("name")=="genero")){
    if(ele.selectedIndex > 0){
      val=true;
    }else{
      aux2="Seleccione una opción de la lista";
    }
  }else if (ele.getAttribute("name")=="sector"){
    if (aux.value.length>=1 && aux.value.length<=30){
      val=true;
    }else{
      aux2="Este campo debe contener 1 dígitos";
    }
  }else if (ele.getAttribute("name")=="rif" || (ele.getAttribute("name")=="codigo")){
    if (aux.value.length>=10 && aux.value.length<=10){
      val=true;
    }else{
      aux2="Este campo debe contener 10 dígitos";
    }
  } 
  if(val){
    aux.parentElement.parentElement.classList.remove("has-error");
    //aux.parentElement.parentElement.getElementsByClassName("help-block")[0].innerText = "";
  }else{
    aux.parentElement.parentElement.classList.add("has-error");
    //comentar aquii
    //aux.parentElement.parentElement.getElementsByClassName("help-block")[0].innerText = aux2;
    mmodal("Error", aux2, "Ok, Entendido", null);
    aux.scrollIntoView();
    window.scrollTo(window.scrollX, window.scrollY-80);
  }
  return val;
}  