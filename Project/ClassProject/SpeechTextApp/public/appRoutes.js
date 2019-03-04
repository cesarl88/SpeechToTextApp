angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'home',
        url: '/home',
        templateUrl: 'public/components/templates/home.view.html',
        controller: 'HomeController'
    });
    $stateProvider.state({
        name: 'login',
        url: '/login',
        templateUrl: 'public/components/templates/login.view.html',
        controller: 'LoginController'
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

    $urlRouterProvider.otherwise('/');
}]);