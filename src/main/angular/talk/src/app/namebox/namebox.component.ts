import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-namebox',
  templateUrl: './namebox.component.html',
  styleUrls: ['./namebox.component.css']
})
export class NameboxComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  record(event:any,bee:string="buns"){
    console.log(event);
    console.log(bee);
  }

}
