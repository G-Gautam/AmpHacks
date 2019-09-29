import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../shared/services/auth.service';

@Component({
  selector: 'app-roommates',
  templateUrl: './roommates.component.html',
  styleUrls: ['./roommates.component.css']
})
export class RoommatesComponent implements OnInit {

  constructor(
    public authService: AuthService
  ) { }

  ngOnInit() {
  }

}
