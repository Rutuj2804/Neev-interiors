(function(n){typeof define=="function"&&define.amd?define(["jquery"],n):typeof module=="object"&&module.exports?module.exports=n(require("jquery")):n(jQuery)})(function(n){var e=Array.prototype.slice,h=Array.prototype.splice,u={topSpacing:0,bottomSpacing:0,className:"is-sticky",wrapperClassName:"sticky-wrapper",center:!1,getWidthFrom:"",widthFromWrapper:!0,responsiveWidth:!1,zIndex:"inherit"},f=n(window),c=n(document),i=[],o=f.height(),r=function(){for(var r,u,h,y,e=f.scrollTop(),l=c.height(),a=l-o,v=e>a?a-e:0,s=0,p=i.length;s<p;s++){var t=i[s],w=t.stickyWrapper.offset().top,b=w-t.topSpacing-v;t.stickyWrapper.css("height",t.stickyElement.outerHeight());e<=b?t.currentTop!==null&&(t.stickyElement.css({width:"",position:"",top:"","z-index":""}),t.stickyElement.parent().removeClass(t.className),t.stickyElement.trigger("sticky-end",[t]),t.currentTop=null):(r=l-t.stickyElement.outerHeight()-t.topSpacing-t.bottomSpacing-e-v,r=r<0?r+t.topSpacing:t.topSpacing,t.currentTop!==r&&(t.getWidthFrom?(padding=t.stickyElement.innerWidth()-t.stickyElement.width(),u=n(t.getWidthFrom).width()-padding||null):t.widthFromWrapper&&(u=t.stickyWrapper.width()),u==null&&(u=t.stickyElement.width()),t.stickyElement.css("width",u).css("position","fixed").css("top",r).css("z-index",t.zIndex),t.stickyElement.parent().addClass(t.className),t.currentTop===null?t.stickyElement.trigger("sticky-start",[t]):t.stickyElement.trigger("sticky-update",[t]),t.currentTop===t.topSpacing&&t.currentTop>r||t.currentTop===null&&r<t.topSpacing?t.stickyElement.trigger("sticky-bottom-reached",[t]):t.currentTop!==null&&r===t.topSpacing&&t.currentTop<r&&t.stickyElement.trigger("sticky-bottom-unreached",[t]),t.currentTop=r),h=t.stickyWrapper.parent(),y=t.stickyElement.offset().top+t.stickyElement.outerHeight()>=h.offset().top+h.outerHeight()&&t.stickyElement.offset().top<=t.topSpacing,y?t.stickyElement.css("position","absolute").css("top","").css("bottom",0).css("z-index",""):t.stickyElement.css("position","fixed").css("top",r).css("bottom","").css("z-index",t.zIndex))}},s=function(){var u,e,t,r;for(o=f.height(),u=0,e=i.length;u<e;u++)t=i[u],r=null,t.getWidthFrom?t.responsiveWidth&&(r=n(t.getWidthFrom).width()):t.widthFromWrapper&&(r=t.stickyWrapper.width()),r!=null&&t.stickyElement.css("width",r)},t={init:function(r){return this.each(function(){var e=n.extend({},u,r),f=n(this),s=f.attr("id"),h=s?s+"-"+u.wrapperClassName:u.wrapperClassName,c=n("<div><\/div>").attr("id",h).addClass(e.wrapperClassName),o;f.wrapAll(function(){if(n(this).parent("#"+h).length==0)return c});o=f.parent();e.center&&o.css({width:f.outerWidth(),marginLeft:"auto",marginRight:"auto"});f.css("float")==="right"&&f.css({float:"none"}).parent().css({float:"right"});e.stickyElement=f;e.stickyWrapper=o;e.currentTop=null;i.push(e);t.setWrapperHeight(this);t.setupChangeListeners(this)})},setWrapperHeight:function(t){var i=n(t),r=i.parent();r&&r.css("height",i.outerHeight())},setupChangeListeners:function(n){if(window.MutationObserver){var i=new window.MutationObserver(function(i){(i[0].addedNodes.length||i[0].removedNodes.length)&&t.setWrapperHeight(n)});i.observe(n,{subtree:!0,childList:!0})}else window.addEventListener?(n.addEventListener("DOMNodeInserted",function(){t.setWrapperHeight(n)},!1),n.addEventListener("DOMNodeRemoved",function(){t.setWrapperHeight(n)},!1)):window.attachEvent&&(n.attachEvent("onDOMNodeInserted",function(){t.setWrapperHeight(n)}),n.attachEvent("onDOMNodeRemoved",function(){t.setWrapperHeight(n)}))},update:r,unstick:function(){return this.each(function(){for(var r=this,u=n(r),f=-1,t=i.length;t-->0;)i[t].stickyElement.get(0)===r&&(h.call(i,t,1),f=t);f!==-1&&(u.unwrap(),u.css({width:"",position:"",top:"",float:"","z-index":""}))})}};window.addEventListener?(window.addEventListener("scroll",r,!1),window.addEventListener("resize",s,!1)):window.attachEvent&&(window.attachEvent("onscroll",r),window.attachEvent("onresize",s));n.fn.sticky=function(i){if(t[i])return t[i].apply(this,e.call(arguments,1));if(typeof i!="object"&&i)n.error("Method "+i+" does not exist on jQuery.sticky");else return t.init.apply(this,arguments)};n.fn.unstick=function(i){if(t[i])return t[i].apply(this,e.call(arguments,1));if(typeof i!="object"&&i)n.error("Method "+i+" does not exist on jQuery.sticky");else return t.unstick.apply(this,arguments)};n(function(){setTimeout(r,0)})})