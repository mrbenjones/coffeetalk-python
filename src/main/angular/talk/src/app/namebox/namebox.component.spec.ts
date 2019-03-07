import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NameboxComponent } from './namebox.component';

describe('NameboxComponent', () => {
  let component: NameboxComponent;
  let fixture: ComponentFixture<NameboxComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NameboxComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NameboxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
