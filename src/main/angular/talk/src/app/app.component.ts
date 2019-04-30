import {Component, EventEmitter, Output} from '@angular/core'
import {ActivatedRoute,Params,Router} from "@angular/router";
import {CallService} from 'src/app/services/call.service';
import {Subscription} from 'rxjs';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})


export class AppComponent {
  vendor: string;
  title: string;
  caller: string;
  code: string;
  activatedRoute: ActivatedRoute;
  callService: CallService;
  sub: Subscription;

  constructor(callservice: CallService, private router:Router,route:ActivatedRoute) {
    this.callService = callservice;
    this.activatedRoute  = route;
  }

  ngOnInit() {

  }

  redirectToCode(code:string){
    alert(code);
  }
}
