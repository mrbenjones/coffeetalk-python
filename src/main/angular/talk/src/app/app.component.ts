import {Component} from '@angular/core'
import {ActivatedRoute,Params} from "@angular/router";
import {CallService} from 'src/app/services/call.service';
import {Subscription} from 'rxjs';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})


export class AppComponent {
  vendor:string;
  title:string;
  caller:string;
  code:string;
  activatedRoute: ActivatedRoute;
  callService: CallService;
  sub: Subscription;

  constructor(callservice: CallService, route:ActivatedRoute) {

    this.callService = callservice;
  }

  ngOnInit() {

    var indata = this.callService.calldata(this.code);

  }

}
