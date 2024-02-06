CREATE TABLE "account_module_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "avatar" varchar(100) NULL, "about_user" text NULL, "address_user" text NULL, "email_active_code" varchar(100) NULL);

CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);

CREATE TABLE "account_module_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "account_module_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);

CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);

CREATE TABLE "account_module_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "account_module_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "article_module_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(300) NOT NULL, "slug" varchar(400) NOT NULL, "image" varchar(100) NOT NULL, "short_description" text NOT NULL, "text" text NOT NULL, "is_active" bool NOT NULL, "create_date" datetime NOT NULL, "author_id" bigint NULL REFERENCES "account_module_user" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "article_module_articlecat" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "url_title" varchar(200) NOT NULL UNIQUE, "is_active" bool NOT NULL, "parent_id" bigint NULL REFERENCES "article_module_articlecat" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "article_module_articlecomment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "create_date" datetime NOT NULL, "text" text NOT NULL, "article_id" bigint NOT NULL REFERENCES "article_module_article" ("id") DEFERRABLE INITIALLY DEFERRED, "parent_id" bigint NULL REFERENCES "article_module_articlecomment" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "account_module_user" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "article_module_article_selected_categories" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "article_id" bigint NOT NULL REFERENCES "article_module_article" ("id") DEFERRABLE INITIALLY DEFERRED, "articlecat_id" bigint NOT NULL REFERENCES "article_module_articlecat" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "contact_module_contact_us" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "email" varchar(200) NOT NULL, "full_name" varchar(200) NOT NULL, "message" text NOT NULL, "created_date" datetime NOT NULL, "response" text NULL, "is_read_by_admin" bool NOT NULL);

CREATE TABLE "contact_module_userprofile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "image" varchar(100) NOT NULL);

CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "account_module_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);

CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);

CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);

CREATE TABLE "order_module_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "is_paid" bool NOT NULL, "payment_day" date NULL, "user_id" bigint NOT NULL REFERENCES "account_module_user" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "product_module_productbrand" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "is_active" bool NOT NULL, "url_title" varchar(200) NOT NULL);

CREATE TABLE "product_module_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "price" integer NOT NULL, "short_description" varchar(360) NULL, "description" text NOT NULL, "is_active" bool NOT NULL, "is_delete" bool NOT NULL, "slug" varchar(200) NOT NULL UNIQUE, "brand_id" bigint NULL REFERENCES "product_module_productbrand" ("id") DEFERRABLE INITIALLY DEFERRED, "image" varchar(100) NOT NULL);

CREATE TABLE "order_module_orderdetail" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "final_price" integer NULL, "count" integer NOT NULL, "order_id" bigint NOT NULL REFERENCES "order_module_order" ("id") DEFERRABLE INITIALLY DEFERRED, "product_id" bigint NOT NULL REFERENCES "product_module_product" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "product_module_productcategory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "url_title" varchar(200) NOT NULL, "is_active" bool NOT NULL, "is_delete" bool NOT NULL);

CREATE TABLE "product_module_productgallery" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "image" varchar(100) NOT NULL, "product_id" bigint NOT NULL REFERENCES "product_module_product" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "product_module_producttag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "caption" varchar(200) NOT NULL, "product_tag_id" bigint NOT NULL REFERENCES "product_module_product" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "product_module_productvisit" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "ip" varchar(30) NOT NULL, "product_id" bigint NOT NULL REFERENCES "product_module_product" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NULL REFERENCES "account_module_user" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "product_module_product_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "product_id" bigint NOT NULL REFERENCES "product_module_product" ("id") DEFERRABLE INITIALLY DEFERRED, "productcategory_id" bigint NOT NULL REFERENCES "product_module_productcategory" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "site_module_footerlinkbox" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL);

CREATE TABLE "site_module_footerlink" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "url" varchar(500) NOT NULL, "footer_link_box_id" bigint NOT NULL REFERENCES "site_module_footerlinkbox" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "site_module_sitebanner" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "url" varchar(400) NULL, "image" varchar(100) NOT NULL, "is_active" bool NOT NULL, "position" varchar(200) NOT NULL);

CREATE TABLE "site_module_site_setting" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "site_name" varchar(200) NOT NULL, "address" varchar(200) NOT NULL, "phone" varchar(200) NULL, "fax" varchar(200) NULL, "email" varchar(200) NULL, "copy_right" text NOT NULL, "logo" varchar(100) NOT NULL, "site_url" varchar(200) NOT NULL, "about_us_text" text NOT NULL, "is_main_setting" bool NOT NULL);

CREATE TABLE "site_module_slider" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "url_link" varchar(200) NOT NULL, "description" text NOT NULL, "image" varchar(100) NOT NULL, "is_active" bool NOT NULL, "url" varchar(500) NOT NULL);

CREATE TABLE "thumbnail_kvstore" ("key" varchar(200) NOT NULL PRIMARY KEY, "value" text NOT NULL);

CREATE INDEX "account_module_user_groups_group_id_00f978fa" ON "account_module_user_groups" ("group_id");

CREATE INDEX "account_module_user_groups_user_id_8f78a168" ON "account_module_user_groups" ("user_id");

CREATE UNIQUE INDEX "account_module_user_groups_user_id_group_id_08382d24_uniq" ON "account_module_user_groups" ("user_id", "group_id");

CREATE INDEX "account_module_user_user_permissions_permission_id_64a45401" ON "account_module_user_user_permissions" ("permission_id");

CREATE INDEX "account_module_user_user_permissions_user_id_78a92b4c" ON "account_module_user_user_permissions" ("user_id");

CREATE UNIQUE INDEX "account_module_user_user_permissions_user_id_permission_id_72edeb82_uniq" ON "account_module_user_user_permissions" ("user_id", "permission_id");

CREATE INDEX "article_module_articlecat_parent_id_a950c295" ON "article_module_articlecat" ("parent_id");

CREATE INDEX "article_module_articlecomment_article_id_8b192bdc" ON "article_module_articlecomment" ("article_id");

CREATE INDEX "article_module_articlecomment_parent_id_4bdebea2" ON "article_module_articlecomment" ("parent_id");

CREATE INDEX "article_module_articlecomment_user_id_f7b3bc0c" ON "article_module_articlecomment" ("user_id");

CREATE INDEX "article_module_article_author_id_8f8fead7" ON "article_module_article" ("author_id");

CREATE INDEX "article_module_article_selected_categories_articlecat_id_94c19d76" ON "article_module_article_selected_categories" ("articlecat_id");

CREATE UNIQUE INDEX "article_module_article_selected_categories_article_id_articlecat_id_283c9677_uniq" ON "article_module_article_selected_categories" ("article_id", "articlecat_id");

CREATE INDEX "article_module_article_selected_categories_article_id_f3e20638" ON "article_module_article_selected_categories" ("article_id");

CREATE INDEX "article_module_article_slug_0e1761df" ON "article_module_article" ("slug");

CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");

CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");

CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");

CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");

CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");

CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");

CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");

CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");

CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");

CREATE INDEX "order_module_orderdetail_order_id_ba205d21" ON "order_module_orderdetail" ("order_id");

CREATE INDEX "order_module_orderdetail_product_id_fb8473b9" ON "order_module_orderdetail" ("product_id");

CREATE INDEX "order_module_order_user_id_0086a007" ON "order_module_order" ("user_id");

CREATE INDEX "product_module_productbrand_title_66d34145" ON "product_module_productbrand" ("title");

CREATE INDEX "product_module_productcategory_title_ca0ad6b0" ON "product_module_productcategory" ("title");

CREATE INDEX "product_module_productcategory_url_title_9fff4c8c" ON "product_module_productcategory" ("url_title");

CREATE INDEX "product_module_productgallery_product_id_cdb41180" ON "product_module_productgallery" ("product_id");

CREATE INDEX "product_module_producttag_caption_7b2ddef4" ON "product_module_producttag" ("caption");

CREATE INDEX "product_module_producttag_product_tag_id_aaf0c27c" ON "product_module_producttag" ("product_tag_id");

CREATE INDEX "product_module_productvisit_product_id_64f64a04" ON "product_module_productvisit" ("product_id");

CREATE INDEX "product_module_productvisit_user_id_a0c1d507" ON "product_module_productvisit" ("user_id");

CREATE INDEX "product_module_product_brand_id_a34f0820" ON "product_module_product" ("brand_id");

CREATE INDEX "product_module_product_category_productcategory_id_98387865" ON "product_module_product_category" ("productcategory_id");

CREATE INDEX "product_module_product_category_product_id_32834b87" ON "product_module_product_category" ("product_id");

CREATE UNIQUE INDEX "product_module_product_category_product_id_productcategory_id_3717f38e_uniq" ON "product_module_product_category" ("product_id", "productcategory_id");

CREATE INDEX "product_module_product_description_69c36a0f" ON "product_module_product" ("description");

CREATE INDEX "product_module_product_short_description_a87bbf50" ON "product_module_product" ("short_description");

CREATE INDEX "site_module_footerlink_footer_link_box_id_1742f7b8" ON "site_module_footerlink" ("footer_link_box_id");

