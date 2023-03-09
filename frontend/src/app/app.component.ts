import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Movie {
  title: string;
  year: string;
  poster: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  searchTitle = '';
  sortOrder = 'asc';
  isLoading = false;
  movies: Movie[] = [];
  errorMessage = '';

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.sortOrder = "title_asc";
  }

  onSubmit() {
    this.isLoading = true;
    this.movies = [];
    this.errorMessage = '';

    const title = this.searchTitle.trim();

    const url = `http://localhost:5000/api/movies?title=${title}&sort=${this.sortOrder}`;
    this.http.get<any>(url).subscribe(data => {
      
        this.movies = data.movies;
        this.isLoading = false;
    });
  }
}