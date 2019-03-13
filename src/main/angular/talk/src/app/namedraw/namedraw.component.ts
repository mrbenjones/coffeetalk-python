import {Component, OnInit} from '@angular/core';
import * as $ from 'jquery';

@Component({
  selector: 'app-namedraw',
  templateUrl: './namedraw.component.html',
  styleUrls: ['./namedraw.component.css']
})

export class NamedrawComponent implements OnInit {
  caller = 'Ted';
  recipient = 'Bill';
  displayRecipient = '                           ';
  displayEmail = '                             ';
  email = 'bill.s.preston.esq@excellent.net';

  constructor() {
  }

  ngOnInit() {
  }

  transmit() {
    this.rollName(this.recipient, this.email);
  }

  private delay(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  private async rollName(newname: string, newEmail) {

    await this.delay(1000);
    this.displayRecipient = newname;
    this.displayEmail = newEmail;
    $('div.name_output').slideDown('slow');
//    $('div.name_output').css('display','block');
  }

}
