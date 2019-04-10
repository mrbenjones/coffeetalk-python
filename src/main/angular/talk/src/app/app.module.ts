import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {NamedrawComponent} from './namedraw/namedraw.component';
import {RouterModule, Routes} from '@angular/router';
import { AboutComponent } from './about/about.component';
import { BlankComponent } from './blank/blank.component';
import {CallService} from "./services/call.service";

const routes: Routes = [
  {path : '', component:BlankComponent},
  {path : 'about', component:AboutComponent},
  {path : 'call' , component:AppComponent,
  children : [
    {path: 'draw/:code',component:NamedrawComponent}
  ]}
];

@NgModule({
  declarations: [
    AppComponent,
    NamedrawComponent,
    AboutComponent,
    BlankComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(routes)
  ],
  providers: [CallService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
