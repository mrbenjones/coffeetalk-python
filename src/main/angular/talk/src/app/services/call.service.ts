

interface CallData {
  [key: string]: string;
}

export class CallService {

  code: string = "unknown";
  caller: string = "George";
  callee: string = "Martha";
  email: string = "martha@test.xx";
  question: string = "Martha?";

  constructor() {
  }

  calldata(code:string): CallData {
    return {
      'code': code,
      'caller': this.caller,
      'callee': this.callee,
      'email': this.email,
      'question': this.question
    }

  }
}
