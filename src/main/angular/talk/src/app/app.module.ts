import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {NamedrawComponent} from './namedraw/namedraw.component';
import {RouterModule, Routes} from '@angular/router';

// const routes: Routes = [
//   {path: '', component: BlankComponent},
//   {path: 'about', component: AboutComponent}
// ];

@NgModule({
  declarations: [
    AppComponent,
    NamedrawComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
