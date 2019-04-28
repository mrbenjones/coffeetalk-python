import {Observable} from "rxjs";
import {Http} from '@angular/http';
import {Injectable} from '@angular/core';
import {CallData} from "../call-data";
import {HttpClient} from "@angular/common/http";



@Injectable(
)

export class CallService {
baseURI: string = "/engine/get_calls";
  code: string = "unknown";
  caller: string = "George";
  callee: string = "Martha";
  email: string = "martha@test.xx";
  question: string = "Martha?";
  callData:CallData;
  resp: Response;

  constructor(private httpClient: HttpClient) {

  }

  calldata(code: string): Promise<CallData> {
    //  console.log(this.http.get("http://localhost:5000/get_calls/"+code));
    var cd: Promise<CallData> = this.httpClient
      .get<CallData>(this.baseURI + "/" + code).toPromise();

    return cd;
  }
}
