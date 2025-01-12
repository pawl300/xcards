<?php
/**
 * Plugin Name: Twitter Cards
 * Description: A simple plugin to add Twitter Card meta tags to your posts.
 * Version: 1.0
 * Author: Your Name
 */

function add_twitter_card_meta() {
    if (is_single()) {
        global $post;
        $title = get_the_title($post->ID);
        $description = get_the_excerpt($post->ID);
        $url = get_permalink($post->ID);
        $image = wp_get_attachment_url(get_post_thumbnail_id($post->ID));

        echo '<meta name="twitter:card" content="summary_large_image" />' . "\n";
        echo '<meta name="twitter:title" content="' . esc_attr($title) . '" />' . "\n";
        echo '<meta name="twitter:description" content="' . esc_attr($description) . '" />' . "\n";
        echo '<meta name="twitter:image" content="' . esc_url($image) . '" />' . "\n";
        echo '<meta name="twitter:site" content="@tezfiles_link" />' . "\n"; // Replace with your Twitter handle
    }
}
add_action('wp_head', 'add_twitter_card_meta');
