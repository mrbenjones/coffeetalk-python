import {Component, EventEmitter, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-blank',
  templateUrl: './blank.component.html',
  styleUrls: ['./blank.component.scss']
})
export class BlankComponent implements OnInit {
  @Output() redirectEvent = new EventEmitter<string>();
  constructor() { }

  ngOnInit() {
  }
    gotoCode(code:string){
      this.redirectEvent.emit(code);
    }



}
