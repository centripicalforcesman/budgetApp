//TODO: move all of this code to its own component. and out of base app.component

import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    standalone: true,
    imports: [RouterModule],
})
export class AppComponent {
    constructor() {
    }
}