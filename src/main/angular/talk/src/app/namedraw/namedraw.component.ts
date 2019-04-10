import {Component, OnInit} from '@angular/core';
import {CallService} from 'src/app/services/call.service';
import {ActivatedRoute} from "@angular/router";
import * as $ from 'jquery';
import {Subscription} from 'rxjs';

@Component({
  selector: 'app-namedraw',
  templateUrl: './namedraw.component.html',
  styleUrls: ['./namedraw.component.css']
})

export class NamedrawComponent implements OnInit {
  caller: string;
  recipient: string;
  email: string;
  question: string;
  code: string;
  callService: CallService = null;
  activatedRoute: ActivatedRoute = null;
  sub: Subscription;

  constructor(callservice: CallService, activatedRoute: ActivatedRoute) {
    this.callService = callservice;
    this.activatedRoute = activatedRoute;

  }

  ngOnInit() {
        this.activatedRoute.params.subscribe(params=>{this.code=params['code'];});
    var indata = this.callService.calldata("aar");
    this.caller = indata['caller'];
    this.recipient = indata['callee'];
    this.email = indata['email'];
    this.question = indata['question'];
    console.log(this.code);

  }

  transmit() {
    this.rollName(this.recipient, this.email);
  }

  private delay(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  private async rollName(newname: string, newEmail) {
    $('div.name_output').slideDown('slow');
  }

}
