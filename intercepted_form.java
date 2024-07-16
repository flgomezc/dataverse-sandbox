// Using the Chrome console to get the form data
var form = document.getElementById('datasetForm');
var formData = new FormData(form);
var jsonObject = {};
formData.forEach((value, key) => {
    jsonObject[key] = value;
});
var jsonString = JSON.stringify(jsonObject, null, 2);  
console.log(jsonString);

// Extracted from the WebIterface filled form:

{
  "datasetForm": "datasetForm",
  "datasetForm:validateFilesOutcome": "",
  "datasetForm:validTermsofAccess": "true",
  "datasetForm:selectHostDataverse_input": "Felipe L Gómez-Cortés SANDBOX Dataverse",
  "datasetForm:selectHostDataverse_hinput": "243",
  "datasetForm:j_idt576:0:j_idt579:0:fieldvaluelist:0:inputText": "Titulo",
  "datasetForm:j_idt576:0:j_idt579:5:j_idt633:0:j_idt635:0:inputText": "Nombre del Autor",
  "datasetForm:j_idt576:0:j_idt579:5:j_idt633:0:j_idt635:1:inputText": "Afiliacion",
  "datasetForm:j_idt576:0:j_idt579:5:j_idt633:0:j_idt635:2:cvv_focus": "",
  "datasetForm:j_idt576:0:j_idt579:5:j_idt633:0:j_idt635:2:cvv_input": "53",
  "datasetForm:j_idt576:0:j_idt579:5:j_idt633:0:j_idt635:3:inputText": "ORCID ID",
  "datasetForm:j_idt576:0:j_idt579:6:j_idt633:0:j_idt635:0:inputText": "Contacto del autor",
  "datasetForm:j_idt576:0:j_idt579:6:j_idt633:0:j_idt635:1:inputText": "afiliacion del autor de contacto",
  "datasetForm:j_idt576:0:j_idt579:6:j_idt633:0:j_idt635:2:inputText": "mail@de.contacto",
  "datasetForm:j_idt576:0:j_idt579:7:j_idt633:0:j_idt635:0:description": "Texto descriptivo",
  "datasetForm:j_idt576:0:j_idt579:7:j_idt633:0:j_idt635:1:inputText": "2024-06-06",
  "datasetForm:j_idt576:0:j_idt579:8:unique2_focus": "",
  "datasetForm:j_idt576:0:j_idt579:8:unique2": "14",
  "datasetForm:j_idt576:0:j_idt579:9:j_idt633:0:j_idt635:0:inputText": "",
  "datasetForm:j_idt576:0:j_idt579:9:j_idt633:0:j_idt635:1:inputText": "",
  "datasetForm:j_idt576:0:j_idt579:9:j_idt633:0:j_idt635:2:inputText": "",
  "datasetForm:j_idt576:0:j_idt579:11:j_idt633:0:j_idt635:0:description": "Related Publication Citation",
  "datasetForm:j_idt576:0:j_idt579:11:j_idt633:0:j_idt635:1:cvv_focus": "",
  "datasetForm:j_idt576:0:j_idt579:11:j_idt633:0:j_idt635:1:cvv_input": "17",
  "datasetForm:j_idt576:0:j_idt579:11:j_idt633:0:j_idt635:2:inputText": "Identificador de la publicacion",
  "datasetForm:j_idt576:0:j_idt579:11:j_idt633:0:j_idt635:3:inputText": "https://url.de.la/publicacion",
  "datasetForm:j_idt576:0:j_idt579:12:fieldvaluelist:0:description": "",
  "datasetForm:j_idt576:0:j_idt579:18:j_idt633:0:j_idt635:0:inputText": "Funding Agency XYZ",
  "datasetForm:j_idt576:0:j_idt579:18:j_idt633:0:j_idt635:1:inputText": "ID funding agency XYZ",
  "datasetForm:j_idt576:0:j_idt579:21:fieldvaluelist:0:inputText": "Gómez-Cortés, Felipe Leonardo",
  "datasetForm:j_idt576:0:j_idt579:22:fieldvaluelist:0:inputText": "2024-07-11",
  "datasetForm:datasetLockedForAnyReasonVariable": "false",
  "datasetForm:datasetStateChangedVariable": "false",
  "datasetForm:fileUpload_input": {},
  "datasetForm:provUpload_input": {},
  "datasetForm:provenanceFreeform": "",
  "datasetForm:termsofAccessHidden": "",
  "datasetForm:fileAccessRequestHidden": "true",
  "datasetForm:requestAccess2_input": "on",
  "datasetForm:termsAccessInput": "",
  "sharrre-total": "0",
  "jakarta.faces.ViewState": "-4741029873318115195:7084328467016380256"
}
