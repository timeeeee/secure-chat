var gulp = require('gulp');
var uglify = require('gulp-uglify');
var browserify = require('gulp-browserify');
var babel = require('gulp-babel');

gulp.task('default', function() {
    return gulp.src(['client.js'])
	.pipe(browserify())
	.pipe(babel({
	    presets: ['env']
	}))
	.pipe(uglify())
	.pipe(gulp.dest('build'))
});

gulp.task('dev', function() {
    return gulp.src(['client.js'])
	.pipe(browserify())
	.pipe(babel({
	    presets: ['env']
	}))
	.pipe(gulp.dest('build'))
}); 
