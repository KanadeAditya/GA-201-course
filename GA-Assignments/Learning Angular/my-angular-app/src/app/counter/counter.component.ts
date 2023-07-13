import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  template:`<h2>Counter: {{ count }}</h2>
  <button (click)="increment()">Increment</button>
  <button (click)="decrement()">Decrement</button>`,
  styleUrls: ['./counter.component.css']
})
export class CounterComponent {
  count = 0;

  increment() {
    this.count++;
  }

  decrement() {
    this.count--;
  }
}
