close all; clear all; clc;

%%
load datamat.mat;

f1 = figure(1);
subplot(2,1,1);
plot(t(1:iter+2), u_ctrl, 'g', t(1:iter+2), u, 'r', ...
             t(1:iter+2), -th(3)*ones(1,iter+2), 'k--', t(1:iter+2), th(3)*ones(1,iter+2), 'k--');
legend('$u_{ctrl}$ : as determined by the controller', ...
    '$u$ : as sent by the controller', 'Interpreter', 'latex');
ylabel('Input $[ms{-2}]$', 'Interpreter', 'latex');
grid minor;

subplot(2,1,2);
plot(t(1:iter+2), u_att, 'b', ...
    t(1:iter+2), -th(3)*ones(1,iter+2), 'k--', t(1:iter+2), th(3)*ones(1,iter+2), 'k--');
legend('$u_{att}$ : input attack profile', 'Interpreter', 'latex');
ylabel('Input attack $[ms{-2}]$', 'Interpreter', 'latex');
xlabel('Time $[s]$', 'Interpreter', 'latex');
grid minor;

l1 = findobj('Type', 'line');
set(l1,'LineWidth',2);

f2 = figure(2);
subplot(3,2,1);
plot(t(1:iter+2), y_sens(1,:), 'g', t(1:iter+2), y(1,:), 'r', ...
               t(1:iter+2), zeros(1,iter+2), 'k--', t(1:iter+2), th(1)*ones(1,iter+2), 'k--');
legend('$y_{sens}$ : sensor outputs', ...
    '$y$ : actual vehicle states', 'Interpreter', 'latex');
ylabel('$d \ [m]$', 'Interpreter', 'latex');
ylim=get(gca,'YLim');
set(gca,'Ylim',[-0.5 ylim(2)]);
grid minor;

subplot(3,2,2);
plot(t(1:iter+2), y_att(1,:), 'b');
legend('$y_{att}$ : output attack profiles', 'Interpreter', 'latex');
ylabel('$d \ [m]$', 'Interpreter', 'latex');
grid minor;

subplot(3,2,3);
plot(t(1:iter+2), y_sens(2,:), 'g', t(1:iter+2), y(2,:), 'r', ...
               t(1:iter+2), zeros(1,iter+2), 'k--', t(1:iter+2), th(2)*ones(1,iter+2), 'k--');
% legend('$y_{sens}$ = v : as measured by the sensor', ...
%     '$y$ = v : actual vehicle output', 'Interpreter', 'latex');
ylabel('$v \ [ms^{-1}]$', 'Interpreter', 'latex');
grid minor;

subplot(3,2,4);
plot(t(1:iter+2), y_att(2,:), 'b');
% legend('$y_{att}$ : output attack profile for velocity', 'interpreter', 'latex');
ylabel('$v \ [ms^{-1}]$', 'Interpreter', 'latex');
grid minor;

subplot(3,2,5);
plot(t(1:iter+2), y_sens(3,:), 'g', t(1:iter+2), y(3,:), 'r', ...
               t(1:iter+2), -th(3)*ones(1,iter+2), 'k--', t(1:iter+2), th(3)*ones(1,iter+2), 'k--');
% legend('$y_{sens}$ = a : as measured by the sensor', ...
%     '$y$ = a : actual vehicle output', 'interpreter', 'latex');
ylabel('$a \ [ms^{-2}]$', 'Interpreter', 'latex');
xlabel('Time $[s]$', 'Interpreter', 'latex');
grid minor;

subplot(3,2,6);
plot(t(1:iter+2), y_att(3,:), 'b');
% legend('$y_{att}$ : output attack profile for acceleration', 'interpreter', 'latex');
ylabel('$v \ [ms^{-1}]$', 'Interpreter', 'latex');
xlabel('Time $[s]$', 'Interpreter', 'latex');
grid minor;

l2 = findobj('Type', 'line');
set(l2,'LineWidth',2);
