// Copyright (C) 2019 Chris Younger


require([
	"splunkjs/mvc",
	"jquery",
	"splunkjs/mvc/simplexml",
	"splunkjs/mvc/layoutview",
	"splunkjs/mvc/simplexml/dashboardview"
], function(
	mvc,
	$,
	DashboardController,
	LayoutView,
	Dashboard
) {

    // Setup the splunk components properly
    $('header').remove();
    var $dashboardBody = $(".dashboard-body");
    var service = mvc.createService({owner: "nobody"});
    new LayoutView({ "hideAppBar": false, "hideChrome": false, "hideFooter": false, "hideSplunkBar": false, layout: "fixed" })
        .render()
        .getContainerElement()
        .appendChild($dashboardBody[0]);

    new Dashboard({
        id: 'dashboard',
        el: $dashboardBody,
        showTitle: true,
        editable: true
    }, { tokens: false }).render();

    DashboardController.ready();

    $(".favicon_changer-img-ico").on("click", function(){
        var ico = $(this).attr('data-ico');
        service.get('/services/favicon_changer?icon=' + ico, null, function(err, r) {
            if (err) {
                showModal({body: err});
            }
            showModal({body: r.data});
        });
    });

	var showModal = function self(o) {
		var options = $.extend({
				title : '',
				body : '',
				remote : false,
				backdrop : true,
				size : 450,
				onShow : false,
				onHide : false,
				actions : false
			}, o);

		self.onShow = typeof options.onShow == 'function' ? options.onShow : function () {};
		self.onHide = typeof options.onHide == 'function' ? options.onHide : function () {};
		if (self.$modal === undefined) {
			self.$modal = $('<div class="modal fade"><div class="modal-dialog"><div class="modal-content"></div></div></div>').appendTo('body');
			self.$modal.on('shown.bs.modal', function (e) {
				self.onShow.call(this, e);
			});
			self.$modal.on('hidden.bs.modal', function (e) {
				self.onHide.call(this, e);
			});
		}
		self.$modal.css({'width': options.size + "px", 'margin-left': -1 * (options.size / 2) + "px"});
		self.$modal.data('bs.modal', false);
		self.$modal.find('.modal-dialog').removeClass().addClass('modal-dialog ');
		self.$modal.find('.modal-content').html('<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">${title}</h4></div><div class="modal-body">${body}</div><div class="modal-footer"></div>'.replace('${title}', options.title).replace('${body}', options.body));

		var footer = self.$modal.find('.modal-footer');
		if (Object.prototype.toString.call(options.actions) == "[object Array]") {
			for (var i = 0, l = options.actions.length; i < l; i++) {
				options.actions[i].onClick = typeof options.actions[i].onClick == 'function' ? options.actions[i].onClick : function () {};
				$('<button type="button" class="btn ' + (options.actions[i].cssClass || '') + '">' + (options.actions[i].label || '{Label Missing!}') + '</button>').appendTo(footer).on('click', options.actions[i].onClick);
			}
		} else {
			$('<button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>').appendTo(footer);
		}
		self.$modal.modal(options);
	};
});
