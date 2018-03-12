module.exports = function(grunt) {
    grunt.initConfig({
        sass: {
            dist: {
                options: {
                    style: 'compressed',
                    debugInfo: true
                },
                files: {
                    'css/style.css': 'scss/style.scss',
                }
            }
        },
        watch: {
            css: {
                files: '**/*.scss',
                tasks: 'sass'
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('default', 'watch');
}