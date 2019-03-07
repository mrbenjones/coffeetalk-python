import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NamedrawComponent } from './namedraw.component';

describe('NamedrawComponent', () => {
  let component: NamedrawComponent;
  let fixture: ComponentFixture<NamedrawComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NamedrawComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NamedrawComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
