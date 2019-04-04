import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';
import { InfoPage } from '../info/info';
import { BuscarPage } from '../buscar/buscar';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  casas: any;
  infoPage = InfoPage;
  buscarPage = BuscarPage;

  constructor(public navCtrl: NavController, public http: HttpClient) {
    this.http.get("/v1/api/v1/casas/")
    .subscribe(data => {
      this.casas = data;
    }, error => {
      console.log(JSON.stringify(error));
    });
  }

  info(casa)
  {
    this.navCtrl.push(this.infoPage, {casa: casa});
  }

  search()
  {
    console.log("Buscar");
    this.navCtrl.push(this.buscarPage, {casas: this.casas});
  }

}
