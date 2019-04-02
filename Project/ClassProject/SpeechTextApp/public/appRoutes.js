angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'home',
        url: '/home',
        templateUrl: 'public/components/templates/home.view.html',
        controller: 'HomeController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/home.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'login',
        url: '/login',
        templateUrl: 'public/components/templates/login.view.html',
        controller: 'LoginController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/login.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'register',
        url: '/register',
        templateUrl: 'public/components/templates/register.view.html',
        controller: 'RegisterController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/register.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'dashboard',
        url: '/dashboard',
        templateUrl: 'public/components/templates/dashboard.view.html',
        controller: 'DashboardController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/dashboard.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'about',
        url: '/about',
        templateUrl: 'public/components/templates/about.view.html',
        controller: 'aboutController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/about.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'profile',
        url: '/profile',
        templateUrl: 'public/components/templates/profile.view.html',
        controller: 'profileController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/profile.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'createTranscript',
        url: '/createTranscript/:filetype',
        templateUrl: 'public/components/templates/createfile.view.html',
        controller: 'createFileController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/createFile.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'TranscriptAudio',
        url: '/TranscriptAudio/:id',
        templateUrl: 'public/components/templates/audiotranscript.view.html',
        controller: 'TranscriptController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/transcript.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'TranscriptVideo',
        url: '/TranscriptVideo/:id',
        templateUrl: 'public/components/templates/videotranscript.view.html',
        controller: 'TranscriptController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/transcript.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'TranscriptMic',
        url: '/TranscriptMic/:id',
        templateUrl: 'public/components/templates/mictranscript.view.html',
        controller: 'TranscriptController',
        controllerAs: 'vm',
        resolve :
        {
            deps:  ['$ocLazyLoad', function($ocLazyLoad){
                return $ocLazyLoad.load({
                    name : 'app',
                    files : [
                        'public/components/controllers/transcript.controller.js'
                    ]
                });
            }]

        }
    });
    $stateProvider.state({
        name: 'register',
        url: '/register',
        templateUrl: 'public/components/templates/register.view.html',
        controller: 'RegisterController'
    });
    $stateProvider.state({
        name: 'dashboard',
        url: '/d',
        templateUrl: 'public/components/templates/dashboard.html',
        controller: 'DashboardController'
    });

    $urlRouterProvider.otherwise('/home');
}]);