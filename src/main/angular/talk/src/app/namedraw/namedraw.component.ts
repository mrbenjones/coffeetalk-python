import {Component, Inject, OnInit} from '@angular/core';
import {CallService} from 'src/app/services/call.service';
import {ActivatedRoute} from "@angular/router";
import * as $ from 'jquery';
import {Subscription} from 'rxjs';
import {CallData} from "../call-data";
import {AboutComponent} from "../about/about.component";

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
  constructor(callservice: CallService, activatedRoute: ActivatedRoute
              ) {
    this.callService = callservice;
    this.activatedRoute = activatedRoute;
  }

  ngOnInit() {
        this.activatedRoute.params.subscribe(params=>{this.code=params['code'];});
        var cd:Promise<CallData> = this.callService.calldata(this.code);
      cd.then(
        s=> {
          console.log(s[0].caller);
          this.caller = s[0].caller;
          this.recipient = s[0].callee;
          this.question = s[0].question;
          this.code = s[0].code;
          this.email = s[0].email;
        }

      );



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
