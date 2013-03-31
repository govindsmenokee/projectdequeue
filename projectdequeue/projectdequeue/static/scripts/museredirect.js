/*
 ADOBE CONFIDENTIAL
 ___________________

 Copyright 2011 Adobe Systems Incorporated
 All Rights Reserved.

 NOTICE:  All information contained herein is, and remains
 the property of Adobe Systems Incorporated and its suppliers,
 if any.  The intellectual and technical concepts contained
 herein are proprietary to Adobe Systems Incorporated and its
 suppliers and may be covered by U.S. and Foreign Patents,
 patents in process, and are protected by trade secret or copyright law.
 Dissemination of this information or reproduction of this material
 is strictly forbidden unless prior written permission is obtained
 from Adobe Systems Incorporated.
*/
typeof Muse=="undefined"&&(Muse={});Muse.Redirect={};Muse.Redirect.domPrefixes=["Webkit","Moz","O","ms","Khtml"];Muse.Redirect.Touch=function(){if(navigator.maxTouchPoints>0)return!0;else for(var b=0,c=Muse.Redirect.domPrefixes.length;b<c;b++){var a=Muse.Redirect.domPrefixes[b]+"MaxTouchPoints";if(a in navigator&&navigator[a])return!0}try{return document.createEvent("TouchEvent"),!0}catch(d){}return!1}();
Muse.Redirect.readCookie=function(b){b+="=";for(var c=document.cookie.split(";"),a=0;a<c.length;a++){for(var d=c[a];d.charAt(0)==" ";)d=d.substring(1,d.length);if(d.indexOf(b)==0)return d.substring(b.length,d.length)}return null};
Muse.Redirect.redirect=function(b,c,a,d){var g=null,f=Muse.Redirect.readCookie("devicelock");f=="phone"&&a?g=a:f=="tablet"&&c&&(g=c);f!=b&&g==null&&(d?d=="phone"&&a?g=a:d=="tablet"&&c&&(g=c):(b=Math.min(screen.width,screen.height)/(window.devicePixelRatio||1),d=window.screen.systemXDPI||0,f=window.screen.systemYDPI||0,d=d>0&&f>0?Math.min(screen.width/d,screen.height/f):0,(b<=370||d!=0&&d<=3)&&a?g=a:b<=960&&c&&Muse.Redirect.Touch&&(g=c)));if(g!=null)document.location=g,document.write('<style type="text/css">body {visibility:hidden}</style>')};
