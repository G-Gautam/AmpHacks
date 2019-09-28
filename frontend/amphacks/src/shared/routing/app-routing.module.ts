import { NgModule } from '@angular/core';
// Required services for navigation
import { Routes, RouterModule } from '@angular/router';

// Import all the components for which navigation service has to be activated 
import { SignInComponent } from '../../app/components/sign-in/sign-in.component';
import { SignUpComponent } from '../../app/components/sign-up/sign-up.component';
import { DashboardComponent } from '../../app/components/dashboard/dashboard.component';
import { ForgotPasswordComponent } from '../../app/components/forgot-password/forgot-password.component';
import { VerifyEmailComponent } from '../../app/components/verify-email/verify-email.component';
import { AuthGuard } from "../../app/shared/guard/auth.guard";
import { SecureInnerPagesGuard } from "../../app/shared/guard/secure-inner-pages.guard.ts.guard";


const routes: Routes = [
  { path: '', redirectTo: '/sign-in', pathMatch: 'full'},
  { path: 'sign-in', component: SignInComponent, canActivate: [SecureInnerPagesGuard]},
  { path: 'register-user', component: SignUpComponent, canActivate: [SecureInnerPagesGuard]},
  { path: 'dashboard', component: DashboardComponent},
  { path: 'forgot-password', component: ForgotPasswordComponent, canActivate: [SecureInnerPagesGuard] },
  { path: 'verify-email-address', component: VerifyEmailComponent, canActivate: [SecureInnerPagesGuard] }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }