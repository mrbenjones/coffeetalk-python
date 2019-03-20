import {Component} from '@angular/core'
import {ActivatedRoute,Params} from "@angular/router";
import {CallService} from 'src/app/services/call.service';
import {Subscription} from 'rxjs';
import {Routes, RouterModule} from '@angular/router';
import {AboutComponent} from "./about/about.component";
import {NamedrawComponent} from "./namedraw/namedraw.component";

const routes:Routes = [
  {path: '', component:AboutComponent},
  {path: 'call/:code' , component:NamedrawComponent}
];

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  vendor:string;
  title:string;
  caller:string;
  code:string;
  activatedRoute: ActivatedRoute;
  callService: CallService;
  sub: Subscription;

  constructor(callservice: CallService, activatedRoute: ActivatedRoute) {
    this.callService = callservice;
    this.activatedRoute = activatedRoute;
  }

  ngOnInit() {

    var indata = this.callService.calldata(this.code);

  }

}
