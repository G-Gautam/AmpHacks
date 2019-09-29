import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-features',
  templateUrl: './features.component.html',
  styleUrls: ['./features.component.css']
})
export class FeaturesComponent implements OnInit {

  constructor() { 
    
  }
  imageArray: any[];
  isImageUploaded: any;
  score: any;

  ngOnInit() {
    this.isImageUploaded = false;
    this.imageArray = new Array();
    this.score = 0;
  }
  onSelectFile(event) { // called each time file input changes
    if (event.target.files && event.target.files[0]) {
      var reader = new FileReader();
      reader.readAsDataURL(event.target.files[0]); // read file as data url
      reader.onload = (event) => { // called once readAsDataURL is completed
        this.imageArray.push(event.target.result);
      }
    }
  }

  getScore(){
    this.score = "Running model";
    setTimeout(()=>{   
      this.score = 8;
 }, 2000);
  }
}